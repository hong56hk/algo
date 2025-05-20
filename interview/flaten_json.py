

def flaten(j, p=""):
  result_dict = {}

  for k in j.keys():
    v = j[k]

    if type(v) is dict:
      d = flaten(v, k)

      for (ik, iv) in d.items():
        tmp = p + "_" + ik if p else ik
        result_dict[tmp] = iv
    else:
      tmp = p + "_" + k if p else k
      result_dict[tmp] = v

  return result_dict



def print_json(j):
  fj = flaten(j)

  print(",".join(fj.keys()))
  value_arr = []
  for k in fj.keys():
    v = fj[k]
    value_arr.append(str(v))
  print(",".join(value_arr))


jj = {
  "key_1": 1,
  "key_2": {
    "key_3": {
      "key_4": 4,
      "key_5": 5
    },
  }
}

print_json(jj)