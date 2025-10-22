from typing import Any

from bson import ObjectId
from pymongo import MongoClient


class MongoTaskRepository:
    def __init__(
        self,
        connection_string: str,
        database_name: str = 'task_manager',
        collection_name: str = 'tasks',
    ) -> None:
        self.client = MongoClient(connection_string)
        self.database = self.client[database_name]
        self.collection = self.database[collection_name]

    def create_task(
        self,
        data: dict[str, Any],
    ) -> str:
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

    def get_task_by_id(
        self,
        task_id: str,
    ) -> dict[str, Any] | None:
        object_id = self.get_object_id(task_id)
        return self.collection.find_one({'_id': object_id})

    def delete_task(
        self,
        task_id: str,
    ) -> bool:
        object_id = self.get_object_id(task_id)
        result = self.collection.delete_one({'_id': object_id})
        return bool(result.deleted_count)

    def aggregate_by_tags(
        self,
    ) -> list[dict[str, Any]]:
        pipeline = [
            {'$match': {'tags': {'$exists': True, '$ne': []}}},
            {'$unwind': '$tags'},
            {'$group': {'_id': '$tags', 'count': {'$sum': 1}}},
            {'$sort': {'count': -1}},
            {'$project': {'tag': '$_id', 'count': 1, '_id': 0}},
        ]

        return list(self.collection.aggregate(pipeline))

    def update_task(
        self,
        task_id: str,
        update_data: dict[str, Any],
    ) -> bool:
        object_id = self.get_object_id(task_id)
        result = self.collection.update_one(
            {'_id': object_id},
            {'$set': update_data},
        )
        return bool(result.matched_count)

    @staticmethod
    def get_object_id(
        task_id: str,
    ) -> ObjectId:
        return ObjectId(task_id)
