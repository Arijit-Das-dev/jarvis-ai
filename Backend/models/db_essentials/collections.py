class MongoClientManager:

    def image_document(self, user_id, user_prompt, date):

        return {
            "user_id":user_id,
            "user_prompt":user_prompt,
            "date":date
        }