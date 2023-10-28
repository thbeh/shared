import rabbitpy

oceanApiUser = "APIACCESS-2172"
oceanApiPassword = "STZ16QWpvjBSfdx4y72QkRZmsUU9HR3e"

# Ocean API hostname, uncomment the relevant one
#oceanApiHostname = "meridian.etrel.com"  # production Ocean instance, https://zero-admin.meridianenergy.co.nz/ gets blocked at the WAF
oceanApiHostname = "stage-meridian.etrel.com" #staging Ocean instance

with rabbitpy.Connection(f'amqps://{oceanApiUser}:{oceanApiPassword}@{oceanApiHostname}:5671/%2F') as conn:
    with conn.channel() as channel:
        # queue = rabbitpy.Queue(channel, f'{oceanApiUser}.helpdesk.ticket.raisedByUser')
        queue = rabbitpy.Queue(channel, f'{oceanApiUser}.*.connector.statusChanged')
        # queue = rabbitpy.Queue(channel, f'{oceanApiUser}.*.*.*.system.event')
        # queue = rabbitpy.Queue(channel, f'{oceanApiUser}.*.session.ended')

        # Exit on CTRL-C
        try:
            # Consume the message
            for message in queue:
                message.pprint(True)
                print(message.body.decode())
                message.ack()

        except KeyboardInterrupt:
            print('Exited consumer')
