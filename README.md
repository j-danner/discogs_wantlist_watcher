#### Discogs Wantlist-Watcher

Python script that checks your discogs wantlist for items on sale that match specified quality and price criteria.

Run `./wantlist_watcher.py -h` to get:

```
usage: wantlist_watcher.py [-h] -tk TOKEN [-sc SLEEVE_CONDITION] [-mc MEDIA_CONDITION] [-i]

Check your discogs wantlist for items on sale meeting a predefined price, stored in the _notes_ section of your
wantlist items.
(If no max price is found, it asks for it and stores it online. BEWARE THIS OVERWRITES NOTES OFWANTLIST ITEMS!)

options:
  -h, --help            show this help message and exit
  -tk TOKEN, --token TOKEN
                        discogs personal access token (can be generated at "discogs.com/settings/developers")
  -sc SLEEVE_CONDITION, --sleeve-condition SLEEVE_CONDITION
                        min accepted sleeve-condition
                        (M > NM > VG+ > VG > G+ > G > F > P > Not Graded > Generic > No Cover)
                        (default: No Cover)
  -mc MEDIA_CONDITION, --media-condition MEDIA_CONDITION
                        min accepted sleeve-condition
                        (M > NM > VG+ > VG > G+ > G > F > P > Not Graded) (default: VG)
  -i, --interactive     ask for max prices for items in wantlist where max-price has not yet been selected
                        (default: False)
```

Note that the argument `-tk TOKEN` is mandatory and that the `notes`-field of your wantlist items is used to store the selected max-price. To set a max-price simply put `max price: XXX` in the `notes`-field of the respective wantlist item, or start start the script in interactive mode.

