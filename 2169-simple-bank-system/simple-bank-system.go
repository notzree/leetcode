type Bank struct {
    balance []int64   
    maxIndexedAccount int
}


func Constructor(balance []int64) Bank {
    incr_balance := make([]int64, len(balance)+1)
    for i,v := range balance{
        incr_balance[i+1] = v
    }
    return Bank{
        balance:incr_balance,
        maxIndexedAccount:len(balance),
    }
}

func (b *Bank) validateAccount(account int) bool {
    if account > b.maxIndexedAccount{
        return false
    }
    if account <=0 {
        return false
    }
    return true

}


func (this *Bank) Transfer(account1 int, account2 int, money int64) bool {
    if valid1 := this.validateAccount(account1); !valid1 {
        return valid1
    }
    if valid2 := this.validateAccount(account2); !valid2 {
        return valid2
    }
    account1Balance := this.balance[account1]
    if account1Balance <money {
        return false
    }
    this.balance[account1] -= money
    this.balance[account2] +=money
    return true
}


func (this *Bank) Deposit(account int, money int64) bool {
    if valid :=this.validateAccount(account); !valid {
        return valid
    }
    this.balance[account] += money
    return true
}


func (this *Bank) Withdraw(account int, money int64) bool {
    if valid := this.validateAccount(account); !valid{
        return valid
    }
    accountBalance :=this.balance[account]
    if accountBalance <money {
        return false
    }
    this.balance[account]-=money
    return true
    
}


/**
 * Your Bank object will be instantiated and called as such:
 * obj := Constructor(balance);
 * param_1 := obj.Transfer(account1,account2,money);
 * param_2 := obj.Deposit(account,money);
 * param_3 := obj.Withdraw(account,money);
 */