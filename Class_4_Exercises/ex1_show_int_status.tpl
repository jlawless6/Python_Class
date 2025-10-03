Value INTERFACE (\S+)

Start
  ^Port.+Type.* -> INT

INT
  ^${INTERFACE}\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+$$ -> Record

EOF