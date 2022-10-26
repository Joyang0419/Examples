# not fit SRP

class SMSService:

    @staticmethod
    def send_message():
        print("使用中華電信送出訊息。")
        print("mysql寫入已發送成功log.")


#  如果現在send_message時，有些log想寫入ElasticSearch, 有些想寫入mysql? 怎麼辦呢?


# fit SRP
class SMSServiceUpdated:

    @staticmethod
    def send_message():
        print("使用中華電信送出訊息。")

    @staticmethod
    def save_log_to_mysql():
        print("mysql寫入已發送成功log.")

    @staticmethod
    def save_log_to_els():
        print("els寫入已發送成功log.")


if __name__ == "__main__":
    SMSServiceUpdated.send_message()
    SMSServiceUpdated.save_log_to_els()
