import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials


def connectToDatabase():
    """Connect to the firestore database

    Returns:
        [firestore client] -- Instance of the firestore database client
    """
    cred = credentials.Certificate('./secrets/firestore.json')
    firebase_admin.initialize_app(cred)
    return firestore.client()
