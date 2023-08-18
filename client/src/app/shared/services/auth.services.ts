import { Injectable } from "@angular/core";
import { RegisterUser, Token, User } from "../interfaces";
import { HttpClient, HttpParams } from '@angular/common/http'
import { Observable, tap } from "rxjs";
import { environment } from '../../../environments/environment'

@Injectable({
    providedIn:'root'
})
export class AuthService{
    apiUrl = environment.apiServer
    private token = '' 
    
    constructor(private http:HttpClient){

    }

    register(user:RegisterUser):Observable<RegisterUser>{
        const body = {
            'name': user.username,
            'email': user.email,
            'password': user.password
        }

            console.log(body);
            
        return this.http.post<RegisterUser>(this.apiUrl + '/api/user/', body)
    }
    // {"access_token": access_token, "token_type": "bearer"}
    login(user:User):Observable<Token>{
        console.log(user,22222);
        const body = new HttpParams()
            .set('username', user.username)
            .set('password', user.password)
            .set('grant_type', 'password')
        return this.http.post<Token>(this.apiUrl + '/api/login/', body)
        .pipe(
            tap(
                (token_obj)=>{
                    console.log(token_obj['access_token']);
                    
                    localStorage.setItem('auth-token', 'Bearer' + ' ' + token_obj['access_token'])
                    this.setToken(token_obj)
                }
            )
        )
    }

    setToken(token_obj:any){
        this.token = 'Bearer' + ' ' + token_obj['access_token']
    }

    setPlainToken(token:string){
        this.token = token
    }

    getToken():string{
        return this.token
    }

    isAuthenticated():boolean{
        return !!this.token
    }

    logout(){
        this.setPlainToken('')
        localStorage.clear()
    }

}

