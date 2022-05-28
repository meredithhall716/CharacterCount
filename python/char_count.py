def char_count(str):
  # Your code here
  new_str = "".join(sorted(str.replace(" ","")))

  letters = {}

  for x in new_str:
    if x in letters:
      letters[x] += 1
    else:
      letters.update({x:1})
  
  answer = []
  for j,i in letters.items():
    answer.append([j] + [i])
  answer = sorted(answer, key = lambda x:x[1], reverse = True)


  return answer

  