import requests
import concurrent.futures

def banner():
    print('''
\033[95m
	⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⡆⢇⠀⢀⠀⠀⠀⠀⢰⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
	⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣠⣴⣛⣯⣿⢿⣿⣿⠤⣼⣦⣤⣄⠀⣸⡄⠀⢸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
	⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠀⣰⡖⢺⡇⢠⣿⣏⢹⣷⣺⣿⣿⢀⣯⣿⣹⠉⣽⣿⣷⢤⣿⣿⣞⣀⣠⠆⠀⠀⠀⣠⠀⠀⠀⠀⠀⠀
	⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣧⣾⡿⣿⢿⣷⣜⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣞⣿⣿⣷⡟⠷⣤⣀⢀⣼⠃⠀⠀⠀⠀⠀⠀
	⠀⠀⠀⠀⠀⢠⠀⢣⣤⣶⠻⣧⣤⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣹⣿⣁⣼⠟⠑⣤⠞⠀⠀⠀⠀⠀
	⠀⠀⠀⠀⢠⠀⢣⣠⡟⣿⣷⣾⣿⣿⣿⠿⢛⣿⣿⣿⠿⠟⠛⠋⠙⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣥⣶⣿⣿⣦⢞⡟⣲⠇⢠⠆⢰⠀
	⠀⠀⠀⠀⠘⣦⠞⣩⣿⣿⣿⣿⡿⠟⠁⣰⣿⡿⠋⠁⠀⢀⣠⣤⣤⣤⣀⡀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣷⣶⠟⣱⡯⠀
	⠀⠀⠀⠈⣰⣻⣿⣿⣿⣿⣿⡿⠁⠀⢰⣿⡟⠀⠀⢀⣴⣿⠿⠛⠛⠻⢿⣿⣶⡀⠀⠀⠹⣿⣯⡿⣿⣿⣿⣿⣿⣯⣟⣿⣿⡶⣋⣴⠋
	⠀⢀⡀⣰⣿⣿⣷⠿⠟⢸⣿⡇⠀⠀⣾⣿⡃⠀⠀⢸⣿⣇⣀⣤⣄⠀⠀⠙⢿⣿⡄⠀⠀⢹⣿⡍⣆⠹⢿⣿⣿⣿⣿⢿⣿⡿⠛⠁⠀
	⠀⠀⣹⣿⣿⣿⢣⣦⠀⢸⣿⣇⠀⠀⠸⣿⣧⡀⠀⠈⠻⠿⠛⢻⣿⣧⠀⠀⠘⣿⣧⠀⠀⢸⣿⣧⠇⠀⠀⣺⡿⣿⣿⣿⣷⣶⣾⠟⠁
	⢀⣴⣿⣿⡞⢡⣇⢧⠀⠀⢿⣿⡄⠀⠀⠙⣿⣷⣤⣀⣀⣀⣤⣾⣿⠃⠀⠀⣸⣿⡇⠀⠀⣸⣿⠏⠀⠀⣰⣿⣷⣮⣿⠙⣯⡯⠀⠀⠀
	⠙⠛⢡⡟⢹⡀⢻⡛⣄⠀⠈⢻⣿⣦⡀⠀⠀⠙⠛⠿⠿⠿⠟⠋⠁⠀⢀⣴⣿⡟⠁⠀⣴⡿⠁⠀⢀⣰⣿⣯⣿⢻⡛⣿⡟⠀⠀⠀⠀
	⠀⠀⡞⢧⣘⣳⠤⣏⡙⠳⠤⢄⣙⣿⣿⣶⣤⣄⣀⣀⣀⣀⣀⣀⣤⣶⣿⡿⠋⢀⣠⠞⠉⠀⣠⣶⣿⡿⢿⠿⣷⣰⠃⣿⠀⠀⠀⠀⠀
	⠀⠀⠘⠲⣤⣤⣶⠃⢉⡷⠶⣤⣤⣉⣉⡛⠛⠿⠿⡿⢿⣿⠿⠿⠛⠋⠁⠀⠒⢋⣤⣤⡶⣾⣿⢿⡗⣍⠈⠇⢹⠇⣸⠇⠀⠀⠀⠀⠀
	⠀⠀⠀⠀⢠⣤⣬⣟⡻⢄⠀⡴⠋⢉⢟⡿⢿⣿⡷⢷⣶⡿⢷⣼⣾⣶⡾⢷⢾⣿⠙⣿⡓⣄⢻⣎⠛⠈⠁⣠⠊⣰⠏⠀⠀⠀⠀⠀⠀
	⠀⠀⠀⠀⠺⠋⠙⠿⣯⡓⢾⣃⠀⠸⡏⠀⠸⠱⠁⠀⢻⠃⢸⡾⣞⡆⢻⠀⢿⣟⣷⠘⠗⠈⢻⠟⠀⣠⠞⠁⡴⠋⠀⠀⠀⠀⠀⠀⠀
	⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠦⠈⠑⠲⢅⣀⠀⠀⠀⠀⠸⠀⠹⡇⠛⠃⠀⠀⠈⠉⢻⠀⠀⠀⠠⠗⠊⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀
	⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠒⠢⠄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
	⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠒⠒⠀⠀Searching the Abyss...⠀⠀⠀⠀⠀
         			     
\033[0m''')

def search_username(username):
    WEBSITES = [
        f'https://www.twitter.com/{username}',
        f'https://www.youtube.com/{username}',
        f'https://{username}.blogspot.com',
        f'https://www.reddit.com/user/{username}',
        f'https://{username}.wordpress.com',
        f'https://www.pinterest.com/{username}',
        f'https://www.github.com/{username}',
        f'https://{username}.tumblr.com',
        f'https://www.flickr.com/people/{username}',
        f'https://steamcommunity.com/id/{username}',
        f'https://vimeo.com/{username}',
        f'https://soundcloud.com/{username}',
        f'https://disqus.com/by/{username}',
        f'https://medium.com/@{username}',
        f'https://{username}.deviantart.com',
        f'https://vk.com/{username}',
        f'https://about.me/{username}',
        f'https://imgur.com/user/{username}',
        f'https://flipboard.com/@{username}',
        f'https://slideshare.net/{username}',
        f'https://fotolog.com/{username}',
        f'https://open.spotify.com/user/{username}',
        f'https://www.mixcloud.com/{username}',
        f'https://www.scribd.com/{username}',
        f'https://www.badoo.com/en/{username}',
        f'https://www.patreon.com/{username}',
        f'https://bitbucket.org/{username}',
        f'https://www.dailymotion.com/{username}',
        f'https://www.etsy.com/shop/{username}',
        f'https://cash.me/{username}',
        f'https://www.behance.net/{username}',
        f'https://www.instagram.com/{username}',
        f'https://www.facebook.com/{username}',
        f'https://www.goodreads.com/{username}',
        f'https://www.instructables.com/member/{username}',
        f'https://keybase.io/{username}',
        f'https://kongregate.com/accounts/{username}',
        f'https://{username}.newgrounds.com',
        f'https://www.wattpad.com/user/{username}',
        f'https://500px.com/{username}',
        f'https://buzzfeed.com/{username}',
        f'https://www.tripadvisor.com/members/{username}',
        f'https://{username}.hubpages.com',
        f'https://www.ebay.com/usr/{username}',
        f'https://facebook.com/{username}',
        f'https://twitter.com/{username}',
        f'https://t.me/{username}',
        f'https://youtube.com/{username}',
        f'https://www.pornhub.com/model/{username}',
        f'https://instagram.com/{username}',
        f'https://www.tiktok.com/{username}',
        f'https://github.com/{username}',
        f'https://www.linkedin.com/in/{username}',
        f'https://plus.google.com/{username}',
        f'https://pinterest.com/{username}',
        f'https://flickr.com/people/{username}',
        f'https://hashnode.com/@{username}',
        f'https://medium.com/@{username}',
        f'https://hackerone.com/{username}',
        f'https://imgur.com/user/{username}',
        f'https://open.spotify.com/user/{username}',
        f'https://pastebin.com/u/{username}',
        f'https://wattpad.com/user/{username}',
        f'https://codecademy.com/{username}',
        f'https://www.wikipedia.org/wiki/User:{username}',
        f'https://{username}.blogspot.com/',
        f'https://{username}.tumblr.com/',
        f'https://{username}.wordpress.com/',
        f'https://steamcommunity.com/id/{username}',
        f'http://www.zone-h.org/archive/notifier={username}',
    ]

    banner()
    print(f'\033[96m[+] Searching for username: {username}\n')

    count = 0
    match = True

    def check_url(url):
        nonlocal match
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()

            if match:
                print('\033[93m[+] FOUND MATCHES')
                match = False

            print(f'\n\033[92m{url} - {response.status_code} - OK')

            if username in response.text:
                print(f'\033[92mPOSITIVE MATCH: Username {username} - text has been detected in the URL.')
            else:
                print(f'\033[91mPOSITIVE MATCH: Username {username} - text has NOT been detected in the URL, could be a FALSE POSITIVE.')

        except requests.exceptions.RequestException as e:
            print(f'\033[91mError while accessing {url}: {e}')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(check_url, WEBSITES)

    total = len(WEBSITES)
    print(f'\n\033[96mFINISHED: A total of {total - 1} MATCHES found out of {total} websites.')

def main():
    banner()
    username = input('\033[92m{+} Enter username to search: ').strip()
    print('\n')

    search_username(username)

if __name__ == '__main__':
    main()
