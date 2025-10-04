Value INT_NAME (\S+)
Value LINE_STATUS ((up|down))
Value ADMIN_STATE ((up|down))
Value MAC_ADDRESS (\S+)
Value MTU (\d+)
Value DUPLEX ((full|half))
Value SPEED (\d+\s.+)

Start
  ^${INT_NAME}\sis\s${LINE_STATUS}
  ^admin.+${ADMIN_STATE}
  ^  Hardware: .+address: ${MAC_ADDRESS}
  ^  MTU ${MTU}
  ^  ${DUPLEX}-duplex, ${SPEED} -> Record

EOF