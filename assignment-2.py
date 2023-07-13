print("=== Task1 ===")
def find_and_print(messages):
 for key, data in messages.items():
  if "18 years old" in data or "college student" in data or "legal age" in data or "vote" in data:# 判斷方法：1. Bob 說自己18歲，無異議；2. Copper以常態情況而言，他是大學生，因此理論上他已超過17歲(除非他是天才跳級生，但這邊無更多判斷資訊，故以正常情況做判斷) 3. Leslie達台灣法定年齡，台灣法定年齡是18歲，故確定他大於17歲。4. Vivian:這邊分為兩個時間點：a. 他說他自己要投票的時候，已經滿18歲 b. 他下周才滿18歲，剛好達可以投票的年齡。以這邊給的資料，他相當可能是>17歲。由於題目敘述方式是most probably older than 17 years old，故納入。Mary和Jenny給的只是一般敘述句，無法判斷年齡，故不納入。
   print(key)

find_and_print({
"Bob":"My name is Bob. I'm 18 years old.",
"Mary":"Hello, glad to meet you.",
"Copper":"I'm a college student. Nice to meet you.",
"Leslie":"I am of legal age in Taiwan.",
"Vivian":"I will vote for Donald Trump next week",
"Jenny":"Good morning."
})
print("=== Task2 ===")
def calculate_sum_of_bonus(data):
# 以績效而言，above average 給2個月薪水的獎金，average給1個月薪水的獎金，below average給0.5個月薪水的獎金
# 以職稱而言，Engineer給6%薪水的獎金，CEO給7%薪水的獎金，Sales給5%薪水的獎金
  exchange_rate = 30
  total_bonus = 0
  for employee in data["employees"]:
    salary = employee["salary"]
    if isinstance(salary,str) and "USD" in salary:#會設定這個條件，是避免萬一salary的型別是int,而USD是str，會產生typeerror
      salary = int(salary.strip("USD")) * exchange_rate
    elif isinstance(salary,str) and "," in salary:
      salary = int(salary.replace(",",""))
    bonus = 0
    if employee["role"]=="Engineer":
      bonus = int(salary * 0.06)
    elif employee["role"]=="CEO":
      bonus = int(salary * 0.07)
    elif employee["role"]=="Sales":
      bonus = int(salary * 0.05)
    
    if employee["performance"]=="above average":
      bonus = int(bonus * 2)
    elif employee["performance"]=="average":
      bonus = int(bonus * 1)
    elif employee["performance"]=="below average":
      bonus = int(bonus * 0.5)
    total_bonus += bonus
  print(total_bonus)         

calculate_sum_of_bonus({
"employees":[
{
"name":"John",
"salary":"1000USD",
"performance":"above average",
"role":"Engineer"
},
{
"name":"Bob",
"salary":60000,
"performance":"average",
"role":"CEO"
},
{
"name":"Jenny",
"salary":"50,000",
"performance":"below average",
"role":"Sales"
}
]
}) # call calculate_sum_of_bonus function
print("=== Task3 ===")
def func(*data):
    middle_letters=[name[1]for name in data]#這邊用陣列，因為陣列可以容納相同元素
    letter_collector=set(middle_letters)#這邊用集合，集合中所有元素只顯示1次，即不會有相同元素
    show_once=False
    for letter in letter_collector:#從集合回推陣列中，每個名字第二個字出現的次數，只顯示一次者，即顯示該名字
        if middle_letters.count(letter) ==1:
            for name in data:
                if name[1]==letter:
                    print(name)
                    show_once=True
    if not show_once:
        print("沒有")

func("彭⼤牆", "王明雅", "吳明")  # print 彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花")  # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")  # print 沒有
print("=== Task4 ===")
def get_number(index):
    list = [0]
    for i in range(1,index+1):
        if i % 2 == 1:# 這邊要用i，不能用index來做計算，因為邏輯上會是先判斷index是奇數還偶數項，然後決定他的數列排序方式，如get_number(5)，用index做為計算基準，數列會變成[0,4,8,12,16,20]
            list.append(list[i-1]+4)
        else:
            list.append(list[i-1]-1)
    print(list[index]) 
get_number(1) # print 4
get_number(5) # print 10
get_number(10) # print 15
print("=== Task5 ===")
def find_index_of_car(seats, status, number):
    diff_list = []
    for i in range(len(seats)):
        for j in range(len(status)):
            if i == j and status[j] == 1 and seats[i] != 0:
                difference = (seats[i] - number)
                if difference >= 0:
                    diff_list.append(difference)#將差異數列出
            
    if len(diff_list) == 0:
        print("-1")
        return # 返回if len(diff_list) == 0，若非空陣列會繼續執行下方程式，若符合空陣列回傳-1
    min_num = min(diff_list)#取出差異數的最小值
    index = [i for i in range(len(seats)) if abs(seats[i] - number) == min_num]#遍歷seats，找出abs(seats[i] - number) == min_num的索引值
    print(*index)#*可以將[]去掉，僅回傳其中的元素      
find_index_of_car([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2)
find_index_of_car([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4)
find_index_of_car([4, 6, 5, 8], [0, 1, 1, 1], 4)
