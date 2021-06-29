import requests, json

BOARD_ID = 'Is89akxj'
DONE_LISTID = '6088484a9c2e634057303f6c'
TODO_LISTID = '6088484a9c2e634057303f6a'
DOING_LISTID = '6088484a9c2e634057303f6b'

listsonboard = []
cardsonlist = {}
cardslist = []

key = ''
token = ''

class card_tasks:
    
    def get_cardsonlist(listid):
        cardsonlist.clear()
        cardslist.clear()
        url = f'https://api.trello.com/1/lists/{listid}/cards'
        query = {'key': key, 'token': token}   
        response = requests.request("GET",url,params=query).text
        card_ids = json.loads(response)
        
        i = 0
        while (len(card_ids)) > i:
            id = card_ids[i]['shortUrl'].split("/")[-1].strip()
            cardname = card_ids[i]['name']
            carddescription = card_ids[i]['desc']
            card = (cardname, id, carddescription)
            cardsonlist.update({'name':cardname,'id':id,'desc':carddescription})
            cardslist.append(list(cardsonlist.values()))   
            i = i + 1 

    def update_card(cardid,listid):
            url = f'https://api.trello.com/1/cards/{cardid}'
            query = { 'key': key, 'token': token,'idList': listid}   
            response = requests.request("PUT",url,params=query)
            return str(response.status_code)

    def addcard_todo(cardname,description):
        url = f'https://api.trello.com/1/cards'
        query = { 'key': key, 'token': token, 'idList': TODO_LISTID, 'name': {cardname}, 'desc': {description}}   
        response = requests.request("POST",url,params=query)
        return str(response.status_code)
        