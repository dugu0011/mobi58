from .models import DynamicData

def tkt_id(is_raise_ticket,userid):
    print(is_raise_ticket)
    print(id)
    if is_raise_ticket == "YES":
        try:
            obj=DynamicData.objects.filter(is_active=True).last()#get(user=userid, is_active=True)
            prefix_number=obj.prefix_txn
            prefix_number=int(prefix_number)
            prefix_number += 1
            obj.prefix_txn = prefix_number
            obj.save()
        except Exception as e:
            prefix_number = 1000
            prefix_number=int(prefix_number)
            prefix_number += 1
            obj=DynamicData.objects.filter(is_active=True).last()
            obj.prefix_txn = prefix_number
            obj.save()
            print(e)
        return prefix_number
    else:

        print("Sorry!")
