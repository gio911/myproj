import { Injectable } from "@angular/core";
import { AuthService } from "../services/auth.services";
import { HttpErrorResponse, HttpEvent, HttpHandler, HttpInterceptor, HttpRequest } from "@angular/common/http";
import { Observable, catchError, throwError } from "rxjs";
import { Router } from "@angular/router";

@Injectable()
export class TokenInterceptor implements HttpInterceptor{
    constructor(private auth:AuthService, private router:Router){

    }

    intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {

        if(this.auth.isAuthenticated()){
            console.log(this.auth.getToken(),667);
            
            req = req.clone({
                setHeaders:{
                    Authorization:this.auth.getToken()
                }
            })
        }
        
        return next.handle(req).pipe(
            catchError(
                (error:HttpErrorResponse)=>this.handleAuthError(error)
            )
        )
    }

    private handleAuthError(error:HttpErrorResponse):Observable<any>{
        if(error.status === 401){
            this.router.navigate(['/login'], {
                queryParams:{
                    tokenExpired:true
                }
            })
        }
        
        return throwError(()=>error)
    }

}