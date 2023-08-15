import { Injectable } from "@angular/core";
import { User } from "../interfaces";
import { HttpClient } from '@angular/common/http'
import { Observable } from "rxjs";
import { environment } from '../../../environments/environment'

@Injectable({
    providedIn:'root'
})
export class AuthService{
    apiUrl = environment.apiServer   
    
    constructor(private http:HttpClient){

    }

    register(){

    }

    login(user:User):Observable<{token:string}>{
        return this.http.post<{token:string}>(this.apiUrl + '/api/login',user)
    }

}

