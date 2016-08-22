MAX_ALLOWABLE_RTT = 30
input_traffic_Bytes = 0
sum_rtt_Tr = 0
num_pkts_with_rtt = 0

def func(p):
  # Accumualte number of bytes
  input_traffic_Bytes += p.size_bytes

  # Track sum of rtt and number of rtt samples
  if (p.rtt < MAX_ALLOWABLE_RTT):
    sum_rtt_Tr += p.rtt
    num_pkts_with_rtt += 1
