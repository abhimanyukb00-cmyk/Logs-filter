
def is_matching_log(log: str, keyword: str):
    return keyword.upper() in log.upper()

class LogsProcessor:
    def log_filter(self, log_batch: dict):
        match_count = 0
        matching_logs = []

        log_list = log_batch["logs"]
        filter_key = log_batch["filter_level"]

        for log in log_list:
            if is_matching_log(log, filter_key):
                matching_logs.append(log)
                match_count += 1

        return {
            "Processed_count":len(log_list),
            "Match_count":match_count,
            "Matching_logs":matching_logs
        }        


            
    
