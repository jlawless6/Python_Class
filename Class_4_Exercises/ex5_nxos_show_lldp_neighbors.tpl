Value DEVICE_ID (\S+)
Value LOCAL_INTF (\S+)
Value CAPABILITY (\S+)
Value PORT_ID (\S+)

Start
  ^Device ID .+Port ID.*$$ -> LLDPtable

LLDPtable
  ^${DEVICE_ID}\s+${LOCAL_INTF}\s+\S+\s+${CAPABILITY}\s+${PORT_ID}.*$$ -> Record

EOF