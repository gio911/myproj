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

    fetchPayments():Observable<Payment[]>{
        return this.http.get<Payment[]>(this.apiUrl+'/api/currentpayments/')
    }

    createPayment(data:Payment):Observable<Payment>{
        return this.http.post<Payment>(this.apiUrl+'/api/currentpayments/', data)
    }

    putPayment(id:number, data:any){
        return this.http.put<any>(this.apiUrl+'/api/currentpayments/'+id, data)
    }

    deleteProduct(id:number){
        return this.http.delete<any>(this.apiUrl+'/api/currentpayments/'+id)
    }
}