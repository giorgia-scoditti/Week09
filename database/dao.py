from database.DB_connect import DBConnect
from model.film import Film

class Dao:
    @staticmethod
    def get_all_film():
        """Query di esempio, non utilizzata dalle funzionalità dell'esercizio."""
        cnx = DBConnect.get_connection()
        try:
            cursor = cnx.cursor(dictionary=True)
            try:
                cursor.execute('''SELECT id, titolo, genere, serata,
                                         numero_voti, somma_voti
                                  FROM film ORDER BY id''')

                result = []
                for r in cursor:
                    film = Film(r['id'], r['titolo'], r['genere'], r['serata'], r['numero_voti'], float(r['somma_voti']))
                    result.append(film)
                return result

            finally:
                cursor.close()
        finally:
            cnx.close()

    @staticmethod
    def read_statistiche(serate):
        """Query di esempio, non utilizzata dalle funzionalità dell'esercizio."""
        cnx = DBConnect.get_connection()
        try:
            cursor = cnx.cursor(dictionary=True)
            try:
                query = ('''SELECT genere, SUM(somma_voti) / SUM(numero_voti) as media_voti, COUNT(*) as numero_film
                            FROM film
                            WHERE serata <= %s
                            GROUP BY genere
                            ORDER BY media_voti ASC''')
                cursor.execute(query, (serate, ))

                result = []
                for r in cursor:
                    result.append(f"{r['genere']}], {r['numero_film']}, {r['media_voti']}")
                return result

            finally:
                cursor.close()
        finally:
            cnx.close()

    @staticmethod
    def read_film_serate(serate):
        """Query di esempio, non utilizzata dalle funzionalità dell'esercizio."""
        cnx = DBConnect.get_connection()
        try:
            cursor = cnx.cursor(dictionary=True)
            try:
                query = ('''SELECT id, titolo, genere, serata,
                                         numero_voti, somma_voti
                            FROM film 
                            WHERE serata <= %s
                            ORDER BY serata''')
                cursor.execute(query, (serate, ))

                result = []
                for r in cursor:
                    film = Film(r['id'], r['titolo'], r['genere'], r['serata'], r['numero_voti'], float(r['somma_voti']))
                    result.append(film)
                return result

            finally:
                cursor.close()
        finally:
            cnx.close()

# Come prima cosa, controllo se la connessione funziona.
if __name__ == "__main__":
    # print(Dao.read_statistiche)
    print(Dao.read_film_serate(3))