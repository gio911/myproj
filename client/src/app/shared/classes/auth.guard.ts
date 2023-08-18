import { ActivatedRouteSnapshot, CanActivate, CanActivateChild, Router, RouterStateSnapshot, UrlTree } from "@angular/router";
import { AuthService } from "../services/auth.services";
import { Observable, of } from "rxjs";
import { Injectable } from "@angular/core";


@Injectable({
    providedIn:'root'
})
export class AuthGuard implements CanActivate, CanActivateChild{

    constructor(private auth:AuthService, private router:Router){

    }

    canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): Observable<boolean>{
        if(this.auth.isAuthenticated()){
            return of(true)
        }else{
            this.router.navigate(['/login'], {
                queryParams:{
                    accessDenide:true
                }
            })
            return of(false)
        }
    }

    canActivateChild(childRoute: ActivatedRouteSnapshot, state: RouterStateSnapshot):Observable<boolean>{
       return this.canActivate(childRoute, state)
    }

}