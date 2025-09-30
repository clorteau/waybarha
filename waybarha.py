#!/usr/bin/env python3
import sys
import json
import argparse
import requests

server = '<your home assistant url>'
token = '<token generated from home assistant in your profile -> settings -> security -> long-lived access tokens>'

def main():
    debug = False
    text = ''
    tooltip = ''
    cssclass = ''
    state = '?'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    parser = argparse.ArgumentParser(
        prog = 'waybarha.py',
        description = 'Waybar home assistant module to query/toggle an entity',
    )
    parser.add_argument('-t', '--toggle', default=False, action='store_true', help='toggle entity on/off; entity\'s state will be read if omitted')
    parser.add_argument('entity', const=None, type=str, help='entity to read or toggle - ex: \'switch.lamp\'')
    args = parser.parse_args()

    if args.toggle:
        response = requests.post(f'{server}/api/services/switch/toggle', headers=headers, json={ 'entity_id': args.entity })
        if (debug): sys.stderr.write(response.text)
        if response.status_code == 200:
            text = '✓'
            tooltip = ''
        else:
            text = ''
            tooltip = json.dumps(response.json())
    else:
        response = requests.get(f'{server}/api/states/{args.entity}', headers=headers)
        if (debug): sys.stderr.write(response.text)
        if response.status_code == 200:
            j = response.json()
            if args.entity.startswith('switch.'):
                if 'attributes' in j:
                    if 'friendly_name' in j['attributes']:
                        text = j['attributes']['friendly_name']
                if 'state' in j:
                    state = j['state']
                    cssclass = state
            else:
                if 'state' in j:
                    text = j['state']
            if (debug): sys.stderr.write(f'{args.entity} is {state}\n')
            tooltip = json.dumps(j)
        else:
            text = ' '
            tooltip = response.text

    output_json = {
        'text': text,
        'state': state,
        'class': cssclass,
        'tooltip': tooltip
    }
    out = json.dumps(output_json)
    if (debug): sys.stderr.write(out)
    print(out)

if __name__ == '__main__':
    main()