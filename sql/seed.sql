-- Script de Carga Inicial (Seed) com Dados Verídicos de Alagoas (Maceió e Arapiraca)
-- Projeto Integrador IV-B · Sistema de Consulta a Pontos de Vacinação em Alagoas

-- 1. Criação do Estado de Alagoas
INSERT INTO states (id, name, uf) 
VALUES (1, 'Alagoas', 'AL') 
ON CONFLICT (id) DO NOTHING;

-- 2. Cidades Obrigatórias da Especificação
INSERT INTO cities (id, state_id, name) VALUES 
(1, 1, 'Maceió'),
(2, 1, 'Arapiraca')
ON CONFLICT (id) DO NOTHING;

-- 3. Catálogo de Imunobiológicos do Calendário Nacional de Vacinação
INSERT INTO vaccines (id, name, description) VALUES
(1, 'Pólio', 'Vacina Poliomielite 1, 2 e 3 (inativada/atenuada) - Proteção contra paralisia infantil'),
(2, 'Sarampo', 'Vacina Tríplice Viral - Sarampo, Caxumba e Rubéola'),
(3, 'Covid-19', 'Vacina contra Covid-19 monovalente/bivalente'),
(4, 'Influenza', 'Vacina contra o vírus da Gripe'),
(5, 'BCG', 'Vacina contra formas graves de tuberculose'),
(6, 'Hepatite B', 'Vacina recombinante contra o vírus da Hepatite B'),
(7, 'Febre Amarela', 'Vacina de vírus atenuado contra Febre Amarela')
ON CONFLICT (id) DO NOTHING;

-- 4. Postos de Vacinação Verídicos de Maceió (ID da Cidade = 1) e Arapiraca (ID = 2)
INSERT INTO vaccination_points (id, city_id, name, neighborhood, logradouro, number, cep, address, latitude, longitude) VALUES
(10, 1, 'UBS Jacintinho', 'Jacintinho', 'Av. Cleto Campelo', 's/n', '57041-000', 'Av. Cleto Campelo, s/n', -9.6412, -35.7289),
(11, 1, 'PAM Salgadinho', 'Poço', 'Rua Mizael Domingues', 's/n', '57025-050', 'Rua Mizael Domingues, s/n', -9.6645, -35.7312),
(12, 1, 'USF Ponta Verde', 'Ponta Verde', 'Rua Dep. José Lages', '240', '57035-330', 'Rua Dep. José Lages, 240', -9.6580, -35.7025),
(20, 2, 'UBS Primavera Arapiraca', 'Primavera', 'Rua Brasília', '100', '57304-000', 'Rua Brasília, 100', -9.7521, -36.6610)
ON CONFLICT (id) DO NOTHING;

-- 5. Vinculação das Vacinas Ofertadas em Cada Ponto de Atendimento
INSERT INTO point_vaccines (point_id, vaccine_id) VALUES
-- UBS Jacintinho (Pólio, Sarampo, Covid-19)
(10, 1), (10, 2), (10, 3),

-- PAM Salgadinho (Pólio, Sarampo, Covid-19, Influenza, BCG, Hepatite B, Febre Amarela)
(11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7),

-- USF Ponta Verde (Covid-19, Influenza)
(12, 3), (12, 4),

-- UBS Primavera Arapiraca (Pólio, Influenza)
(20, 1), (20, 4)
ON CONFLICT DO NOTHING;

-- 6. Administrador Inicial Padrão (username: admin / senha: admin123)
-- Hash Bcrypt gerado para 'admin123'
INSERT INTO admin_users (id, username, hashed_password) VALUES
(1, 'admin', '$2b$12$Dgb8lfETvVgFGLb6zDUTrugLqz5G0uX1CzXZ5Pb2pjBgEXLzLFcYO')
ON CONFLICT (username) DO UPDATE SET hashed_password = EXCLUDED.hashed_password;

-- Ajusta as sequências dos IDs gerados automaticamente
SELECT setval('states_id_seq', (SELECT COALESCE(MAX(id), 1) FROM states));
SELECT setval('cities_id_seq', (SELECT COALESCE(MAX(id), 1) FROM cities));
SELECT setval('vaccines_id_seq', (SELECT COALESCE(MAX(id), 1) FROM vaccines));
SELECT setval('vaccination_points_id_seq', (SELECT COALESCE(MAX(id), 1) FROM vaccination_points));
SELECT setval('admin_users_id_seq', (SELECT COALESCE(MAX(id), 1) FROM admin_users));
