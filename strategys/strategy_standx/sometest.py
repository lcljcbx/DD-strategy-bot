import time

def some():
    print("some")
    print("平仓完成，进入休眠 5 秒以避免立即重新建仓...")
    time.sleep(5)
    

def main():
    print("Hello, World!")
    sleep_interval = 2
    i = 1
    while True:
        print(f"第 {i} 轮循环")
        some()
        print(f"\n等待 {sleep_interval} 秒后继续...\n")
        time.sleep(sleep_interval)
        i += 1




if __name__ == "__main__":
    main()