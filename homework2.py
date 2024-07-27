def send_email (message, recipient, sender= "university.help@gmail.com"):

        variants = ('.com', '.ru', '.net')
        if recipient.endswith (variants) and sender.endswith (variants) and '@' in sender and '@' in recipient:
                if variants == sender:
                    print("Нельзя отправить письмо самому себе!")
                else:
                    if sender != "university.help@gmail.com":
                        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <{sender}> на адрес <{recipient}>.")
                    else:
                        print (f"Письмо успешно отправлено с адреса <{sender}> на адрес <{recipient}>.")
        else:
            print(f"Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>.")


send_email ('sdf.ru', 'dsf@.ru')