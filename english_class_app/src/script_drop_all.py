from server.database import Base, engine
from sqlalchemy import MetaData
metadata = MetaData()
metadata.reflect(bind=engine)
metadata.drop_all(bind=engine)
print("Todas as tabelas refletidas foram removidas.")




