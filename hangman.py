def hangman(word):#wordはhangmanを始める際に指定する
    wrong = 0#プレイヤーの間違えた回数
    stages = ["",
              "------    ",
              "|         ",
              "|    |    ",
              "|    O    ",
              "|   /|\   ",
              "|   / \   ",
              "|         "
              ]#文字列のリスト　間違えのたびにハングマンが出てくる
    rletters = list(word)#wordの文字を１文字ずつ分解してリスト化した
    board =["_"] * len(word)#プレイヤーに見せる文字数のヒント
    win = False#winは最初Falseに設定しておく
    print("ハングマンへようこそ！")#開始の合図
    while wrong < len(stages) - 1:#wrongの回数＜リスト表示数　-1はwrongが０から始まる分
        print("\n")#段落
        msg = "1文字を予想してね:"#プレイヤーに入力させる部分の文字
        char = input(msg)#プレイヤーに文字を入力させてcharに渡す
        if char in rletters:#rlettersの中にcharで渡された文字があったら？ということ
            cind = rletters.index(char)#何番目の文字か？ということ。数字がcindに渡される
            board[cind] = char#boardのcind(入力された文字の番号)の位置に文字を出す
            rletters[cind] = '$'#正解した文字は＄に変換することでダブリを防ぐ
        else:
            wrong += 1#不正解の回数を１回増やす
        print(" ".join(board))#スコアボード(_ _ _)を表示
        e = wrong + 1#不正解数+1
        print("\n".join(stages[0:e]))#開始インデックス(0)から終了インデックス(e=wrong+1)までハングマン表示
        if "_" not in board:#全ての文字が明らかになったら
            print("あなたの勝ち！")
            print(" ".join(board))#正解を表示
            win = True#FalseだったwinをTrueにする
            break#終了
    if not win:#winがFalseのままだったら？
        print("\n".join(stages[0:wrong+1]))#ハングマン全表示！
        print("あなたの負け！正解は{}.".format(word))#負け宣言と答えの表示
            
hangman("cat")#ゲームスタート

def hangman(word):
    wrong = 0
    stages = ["",
              "------    ",
              "|         ",
              "|    |    ",
              "|    O    ",
              "|   /|\   ",
              "|   / \   ",
              "|         "
              ]
    rletters = list(word)
    board =["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね:"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は{}.".format(word))
            
hangman("cat")
