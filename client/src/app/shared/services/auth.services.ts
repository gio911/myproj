import { Injectable } from "@angular/core";
import { User } from "../interfaces";
import { HttpClient } from '@angular/common/http'
import { Observable } from "rxjs";

import AppConfig from '../../../app-config'

@Injectable({
    providedIn:'root'
})
export class AuthService{

    apiUrl = AppConfig.settings
    
    
    constructor(private http:HttpClient){

    }

    register(){

    }

    login(user:User):Observable<{token:string}>{
        console.log(this.apiUrl);
        return this.http.post<{token:string}>('/api/login',user)
    }

}

