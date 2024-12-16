""" Module with initial database data """
import logging

from sqlmodel import Session

from app.core.db import engine, init_db
from app.models import Song, userSongLink, User, Album
from datetime import datetime, timedelta

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    with Session(engine) as session:
        init_db(session)

        session.query(Song).delete()
        session.query(User).delete()
        session.query(Album).delete()
        session.query(userSongLink).delete() 
        song1 = Song(
            title="Piratas del Bar Caribe", 
            artist="Melendi",
            album="Curiosa la cara de tu padre",
            duration=timedelta(minutes=4, seconds=5), 
            timestamp=datetime(2008, 9, 16)
        )
        
        song2 = Song(
            title="Tu jardín con enanitos", 
            artist="Melendi",
            album="Lágrimas desordenadas", 
            duration=timedelta(minutes=3, seconds=57), 
            timestamp=datetime(2012, 11, 13)
        )
        
        song3 = Song(
            title="16 Añitos", 
            artist="Dani Martín", 
            album="Pequeño", 
            duration=timedelta(minutes=4, seconds=14), 
            timestamp=datetime(2010, 10, 26)
        )
        
        song4 = Song(
            title="Cero", 
            artist="Dani Martín", 
            album="Grandes éxitos y pequeños desastres", 
            duration=timedelta(minutes=4, seconds=21), 
            timestamp=datetime(2017, 11, 10)
        )
        
        song5 = Song(
            title="Antes de que cuente diez", 
            artist="Fito y Fitipaldis", 
            album="Antes de que cuente diez", 
            duration=timedelta(minutes=4, seconds=46), 
            timestamp=datetime(2009, 9, 16)
        )
        
        song6 = Song(
            title="Por la boca vive el pez", 
            artist="Fito y Fitipaldis", 
            album="Fitografía", 
            duration=timedelta(minutes=4, seconds=30), 
            timestamp=datetime(2017, 11, 10)
        )
        
        song7 = Song(
            title="Sucede", 
            artist="Extremoduro", 
            album="Ágila", 
            duration=timedelta(minutes=3, seconds=6), 
            timestamp=datetime(1996, 2, 23)
        )
        
        song8 = Song(
            title="19 días y 500 noches", 
            artist="Sabina", 
            album="19 días y 500 noches", 
            duration=timedelta(minutes=4, seconds=44), 
            timestamp=datetime(1999, 9, 14)
        )
        
        song9 = Song(
            title="Un violinista en tu tejado", 
            artist="Melendi",
            album="Curiosa la cara de tu padre", 
            duration=timedelta(minutes=3, seconds=41), 
            timestamp=datetime(2008, 9, 16)
        )
        
        song10 = Song(
            title="Lágrimas desordenadas", 
            artist="Melendi",
            album="Lágrimas desordenadas", 
            duration=timedelta(minutes=3, seconds=49), 
            timestamp=datetime(2012, 11, 13)
        )
        
        song11 = Song(
            title="Mira la Vida", 
            artist="Dani Martín", 
            album="Pequeño", 
            duration=timedelta(minutes=3, seconds=40), 
            timestamp=datetime(2010, 10, 26)
        )
        
        song12 = Song(
            title="Eres", 
            artist="Dani Martín", 
            album="Grandes éxitos y pequeños desastres", 
            duration=timedelta(minutes=3, seconds=37), 
            timestamp=datetime(2017, 11, 10)
        )
        
        song13 = Song(
            title="Me equivocaría otra vez", 
            artist="Fito y Fitipaldis", 
            album="Fitografía", 
            duration=timedelta(minutes=5, seconds=6), 
            timestamp=datetime(2017, 11, 10)
        )
        
        song14 = Song(
            title="So payaso", 
            artist="Extremoduro", 
            album="Ágila", 
            duration=timedelta(minutes=4, seconds=41), 
            timestamp=datetime(1996, 2, 23)
        )
        
        song15 = Song(
            title="A Mis Cuarenta y Diez", 
            artist="Sabina", 
            album="19 días y 500 noches", 
            duration=timedelta(minutes=7, seconds=11), 
            timestamp=datetime(1999, 9, 14)
        )

        song16 = Song(
            title="Todo a cien", 
            artist="Fito y Fitipaldis", 
            album="Antes de que cuente diez", 
            duration=timedelta(minutes=3, seconds=50), 
            timestamp=datetime(2009, 9, 16)
        )

        

        # Añadir canciones
        session.add(song1)
        session.add(song2)
        session.add(song3)
        session.add(song4)
        session.add(song5)
        session.add(song6)
        session.add(song7)
        session.add(song8)
        session.add(song9)
        session.add(song10)
        session.add(song11)
        session.add(song12)
        session.add(song13)
        session.add(song14)
        session.add(song15)
        session.add(song16)
        session.commit()


def main() -> None:
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
