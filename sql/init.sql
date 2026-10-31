-- Script DDL de Inicialização do PostgreSQL 16
-- Projeto Integrador IV-B · Sistema de Consulta a Pontos de Vacinação em Alagoas

-- 1. Tabela de Administradores (Autenticação do Módulo Admin)
CREATE TABLE IF NOT EXISTS admin_users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2. Tabela de Estados (Nível 1 da Hierarquia Geográfica)
CREATE TABLE IF NOT EXISTS states (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    uf CHAR(2) NOT NULL UNIQUE
);

-- 3. Tabela de Cidades (Nível 2 da Hierarquia Geográfica)
CREATE TABLE IF NOT EXISTS cities (
    id SERIAL PRIMARY KEY,
    state_id INT NOT NULL REFERENCES states(id) ON DELETE CASCADE,
    name VARCHAR(120) NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_cities_state ON cities(state_id);

-- 4. Tabela de Pontos de Vacinação (Nível 3 da Hierarquia Geográfica)
CREATE TABLE IF NOT EXISTS vaccination_points (
    id SERIAL PRIMARY KEY,
    city_id INT NOT NULL REFERENCES cities(id) ON DELETE CASCADE,
    name VARCHAR(150) NOT NULL,
    neighborhood VARCHAR(100),
    address VARCHAR(200),
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uq_city_point_name UNIQUE (city_id, name)
);
CREATE INDEX IF NOT EXISTS idx_vaccination_points_city ON vaccination_points(city_id);

-- 5. Catálogo de Vacinas
CREATE TABLE IF NOT EXISTS vaccines (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);

-- 6. Tabela Associativa: Pontos de Vacinação <-> Vacinas Ofertadas
CREATE TABLE IF NOT EXISTS point_vaccines (
    point_id INT NOT NULL REFERENCES vaccination_points(id) ON DELETE CASCADE,
    vaccine_id INT NOT NULL REFERENCES vaccines(id) ON DELETE CASCADE,
    PRIMARY KEY (point_id, vaccine_id)
);
CREATE INDEX IF NOT EXISTS idx_point_vaccines_vaccine ON point_vaccines(vaccine_id);
