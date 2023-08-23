export interface User{
    username:string
    password:string
}

export interface RegisterUser extends User{
    email:string
}

export interface Payment{
    id:number
    date:Date
    num:number
    sum:number
    counterparty:string
    contract:string
    purpose?:string
    comment:string
    document?:Uint8Array
}

export interface Token{
    access_token:string
    token_type:string
}