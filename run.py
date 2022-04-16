if __name__=='__main__':
        try:
                __import__("gbff").main()
        except Exception as e:
                exit(str(e))
