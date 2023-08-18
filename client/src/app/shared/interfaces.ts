export interface User{
    username:string
    password:string
}

export interface RegisterUser extends User{
    email:string
}

export interface Payment{
    id:number
    payment_date:Date
    payment_num:number
    payment_sum:number
    counterparty:string
    contract:string
    payment_purpose?:string
    comment:string
}

export interface Token{
    access_token:string
    token_type:string
}