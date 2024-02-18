from flask import Flask, jsonify, request

from wantlist_watcher import check_offers_in_wantlist, parse_price, get_price_stats, Condition

app = Flask(__name__)


#config info
config:dict = { 'token': '',
                'min_media_condition': '',
                'min_sleeve_condition': '',
                'interactive': False
              }

offers:list[dict] = []

#main endpoint
@app.route('/discogs_good_offers', methods=['POST'])
def get_good_offers():
    #return offer if we still have unfetched content
    if len(offers)>0:
        offer = offers.pop(0)
        return jsonify( offer | {'offer_number': len(offers)+1} )
    
    #fill offers with good-offers
    _config = request.get_json()
    request.headers.get('your-header-name')
    if 'Authorization' in request.headers:
        config['token'] = request.headers.get('Authorization')
    else:
        return "token as field 'Authorization' missing in header", 400
    if 'min_media_condition' in _config:
        config['min_media_condition'] = Condition(_config['min_media_condition'])
    if 'min_sleeve_condition' in _config:
        config['min_sleeve_condition'] = Condition(_config['min_sleeve_condition'])
    #scrape discogs
    try:
        good_offers, _ = check_offers_in_wantlist(**config)
    except:
        return jsonify({'title': 'Error in Discogs web-scraping!', 'message': "could not load any good offers... :/", 'offer_number': 0, 'url': "-"}), 400
    for offer in good_offers:
        item = offer['wantlist_item'].release
        title = f'Good offer found for {item.artists[0].name} - {item.title}'
        msg = f'tracklist: { list(i.title for i in item.tracklist) }\n' + f'media condition: {offer["media_condition"]}, sleeve condition: {offer["sleeve_condition"]}\n' + f'price {offer["price"]} (max-price: {parse_price(offer["wantlist_item"])})\n' + f'Marketplace {str(get_price_stats(item.id, url=item.url)).replace("<","").replace(">","")}'
        url = offer['url']
        offers.append( {'title': title, 'message': msg, 'url': url} )
    if len(offers)==0:
        return jsonify({'title': "No good offer found", 'message': "-", 'offer_number': 0, 'url': "-"})
    else:
        offer = offers.pop(0)
        return jsonify( offer | {'offer_number': len(offers)+1} )

