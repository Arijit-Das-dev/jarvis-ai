class MongoDocumentBuilder:

    # IMAGE DATABASE
    def image_document(self, user_id, user_prompt, date):

        return {
            "user_id":user_id,
            "user_prompt":user_prompt,
            "date":date
        }
    
    # EDITOR DATEBASE
    def editor_code_document(self, user_id, user_code, date):

        return {
            "user_id":user_id,
            "user_code":user_code,
            "date":date
        }
    
    # EDITOR DATABASE
    def editor_query_document(self, user_id, user_query, date):

        return {
            "user_id":user_id,
            "user_query":user_query,
            "date":date
        }
    
    def main_db_user_document(self, user_id, user_query, date):

        return {
            "user_id":user_id,
            "user_query":user_query,
            "date":date
        }
    
    def main_db_assistant_document(self, user_id, ai_answer, date):

        return {
            "user_id":user_id,
            "ai_answer":ai_answer,
            "date":date
        }
    
    def prompt_db_user_document(self, user_id, user_query, date):

        return {
            "user_id":user_id,
            "user_query":user_query,
            "date":date
        }
    
    def prompt_db_assistant_document(self, user_id, ai_response, date):

        return {
            "user_id":user_id,
            "ai_response":ai_response,
            "date":date
        }