Value NEIGHBOR (([0-9]{1,3}\.){3}[0-9]{1,3})
Value REMOTE_AS (\d+)
Value UP_DOWN (\S+)
Value STATE_PFXRCD (\S+)
Value Filldown LOCAL_AS (\d+)
Value Filldown BGP_ROUTER_ID (([0-9]{1,3}\.){3}[0-9]{1,3})

Start
  ^BGP.+identifier ${BGP_ROUTER_ID}.+AS number ${LOCAL_AS}.*$$
  ^Neighbor.+State.PfxRcd.*$$ -> NeighborTable

NeighborTable
  ^${NEIGHBOR}\s+\d+\s+${REMOTE_AS}(\s+\d+){5}\s+${UP_DOWN}\s+${STATE_PFXRCD}.*$$ -> Record

EOF