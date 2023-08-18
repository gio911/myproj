import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { environment } from "src/environments/environment";
import { Payment } from "../interfaces";
import { Observable } from "rxjs";

@Injectable({
    providedIn:'root'
})
export class CurrentPaymentsService{

    apiUrl = environment.apiServer

    constructor(private http:HttpClient){

    }

    fetch():Observable<Payment[]>{
        return this.http.get<Payment[]>(this.apiUrl+'/api/currentpayments/')
    }
}