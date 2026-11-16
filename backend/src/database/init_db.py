import os
import logging
from sqlalchemy import text
from src.database.connection import engine
from src.database.models.base import Base
import src.database.models.entities  # Garante registro de todas as entidades

logger = logging.getLogger(__name__)


async def init_database():
    """
    Inicializa as tabelas do banco de dados e executa a carga inicial (seed)
    caso o banco esteja vazio ou recém-criado em serviços gerenciados (como Render).
    """
    try:
        # 1. Criação de tabelas a partir dos modelos SQLAlchemy
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        logger.info("[DB INIT] Tabelas verificadas/criadas com sucesso.")

        # 2. Localização do arquivo de seed.sql
        possible_seed_paths = [
            os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))), "sql", "seed.sql"),
            os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "sql", "seed.sql"),
            os.path.join(os.getcwd(), "sql", "seed.sql"),
            os.path.join(os.path.dirname(os.getcwd()), "sql", "seed.sql"),
            "/app/sql/seed.sql"
        ]

        seed_file = next((path for path in possible_seed_paths if os.path.isfile(path)), None)

        if seed_file:
            with open(seed_file, "r", encoding="utf-8") as f:
                content = f.read()

            statements = [stmt.strip() for stmt in content.split(";") if stmt.strip()]

            async with engine.begin() as conn:
                for stmt in statements:
                    try:
                        await conn.execute(text(stmt))
                    except Exception as stmt_err:
                        # Loga como aviso caso seja conflito de chave ou sequência
                        logger.warning(f"[DB INIT] Aviso ao executar instrução de seed: {stmt_err}")

            logger.info(f"[DB INIT] Seed executado com sucesso a partir de: {seed_file}")
        else:
            logger.warning("[DB INIT] Arquivo sql/seed.sql não localizado nos caminhos mapeados.")

    except Exception as e:
        logger.error(f"[DB INIT ERROR] Falha ao inicializar banco de dados: {e}", exc_info=True)
