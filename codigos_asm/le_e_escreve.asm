data r0, 0x97
data r1, 0x01
data r2, 0xf0
data r3, 0xf5

out addr,r0

in data,r0
st r2,r0
add r1,r2
cmp r3,r2
ja 0x09

data r0,0x98
data r2, 0xf0

out addr, r0

ld r2,r0
out data, r0
add r1,r2
cmp r3,r2
ja 0x14

halt
