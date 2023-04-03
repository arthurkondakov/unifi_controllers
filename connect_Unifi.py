import logging
import sched, time
from pyunifi.controller import Controller

s = sched.scheduler(time.time, time.sleep)


def msk_event():
    s.enter(360, 1, msk_event)
    logging.basicConfig(level=logging.INFO, filename='myapp.log', format='%(asctime)s %(levelname)s:%(message)s')
    try:
        msk = Controller('0.0.0.0', 'login', 'password', ssl_verify=False)
        for user in msk.get_clients():
            try:
                data = ['ap_mac', user['ap_mac'], 'assoc_time', user['assoc_time'], 'latest_assoc_time',
                        user['latest_assoc_time'],
                        "oui", user['oui'], "is_guest", user['is_guest'], 'vlan', user['vlan'],
                        "hostname", user['hostname'], "mac", user['mac'], 'user_id', user['user_id'], 'ip', user['ip'],
                        '1x_identity', user['1x_identity'], "first_seen", user['first_seen'], "last_seen",
                        user['last_seen'],
                        "disconnect_timestamp", user['disconnect_timestamp']]
                logging.info(data)
            except KeyError:
                continue
    except OSError as e:
        logging.error("error reading the file")

msk_event()
s.run()
