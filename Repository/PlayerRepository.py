from sqlalchemy import create_engine , asc, desc , func
from sqlalchemy.orm import sessionmaker

from Repository.IRepository.IPlayerRepository import IPlayerRepository
from Models.PlayerModels.Player import Player


class PlayerRepository(IPlayerRepository):
    
    DATABASE_URL = "mysql+pymysql://root:root@localhost/zao"

    def __init__(self) -> None:
        engine = create_engine(self.DATABASE_URL)
        Session = sessionmaker(bind=engine)
        self.engine = engine
        self.session = Session()

    def getAll(self, order_by_column: str = None, ascending: bool = True, **filters) ->list[Player]:
        """ 
            Example : 
            england_defenders = player_repo.getAll(nationality='England', position='defender')

        """
        query = self.session.query(Player)
        
        if filters:
            for attr, value in filters.items():
                query = query.filter(getattr(Player, attr) == value)
        
        if(order_by_column) :
            if ascending:
                query = query.order_by(asc(getattr(Player, order_by_column)))
            else:
                query = query.order_by(desc(getattr(Player, order_by_column)))
        
        result = query.all()
        
        return result
    
    
    def get(self, order_by_column: str = None, ascending: bool = True, **filters) :
        
        query = self.session.query(Player)

        # Apply filters if provided
        if filters:
            for attr, value in filters.items():
                query = query.filter(getattr(Player, attr) == value)
        
        # Determine the order by column and direction
        if(order_by_column) :
            if ascending:
                query = query.order_by(asc(getattr(Player, order_by_column)))
            else:
                query = query.order_by(desc(getattr(Player, order_by_column)))
        
        # Retrieve the first result based on the ordering
        result = query.first()

        return result
    
    def get_random_entries(self, n: int):
        #limit takes care if the n > number of entries
        random_entries = self.session.query(Player).order_by(func.rand()).limit(n).all()
        return random_entries

    def  get_col_values_count(self, column_name: str):
        column = getattr(Player, column_name, None)

        if column is None:
            raise ValueError(f"Column {column_name} does not exist in Player model")

        value_counts = self.session.query(
            column,
            func.count(column).label('count')
        ).group_by(column).all()

        return dict(value_counts)
    
    def add_player(self ,player:Player):
        self.session.add(player)
        self.session.commit()

    def add_players(self ,players:list[Player]):
        self.session.add_all(players)
        self.session.commit()

    def __del__(self):
            # Perform cleanup operations here
            self.session.close()
            self.engine.dispose()
