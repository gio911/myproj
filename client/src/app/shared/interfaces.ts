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
    document?:Blob
    pdfsrc?:string
    wordsrc?:string
    doccreated?:boolean
    docarchive?:boolean
}

export interface Token{
    access_token:string
    token_type:string
}


export interface Commentment{
    id:number
    date?:Date
    text:string
    isDone?:boolean
    user_id?:number
    payment_id?:number
}