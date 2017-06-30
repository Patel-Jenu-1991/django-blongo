#!/usr/bin/env python3

# Test Script

def main():
    import pymongo

    # Open the MongoDB connection
    conn = pymongo.MongoClient('mongodb://localhost:27017')

    # Print the available MongoDB databases

    databases = conn.database_names()

    for database in databases: print(database)

    # Close the MongoDB connection
    conn.close()
    return None

if __name__ == "__main__": main()
