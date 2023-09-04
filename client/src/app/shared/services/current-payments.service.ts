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

    createPdfFile(id:number, payment:Payment){
        
        console.log(payment, 885858540000);
        
        return this.http.post<any>(this.apiUrl+'/api/currentpayments/create-pdf/'+id, payment)
    }

    fetchPdf(id:number, payment:Payment){
        return this.http.post(this.apiUrl+'/api/currentpayments/fetch-pdf/'+id, payment, {observe:'response', responseType: 'blob' });
    }

    sendEmail(id:number, payment:Payment):Observable<string>{
        return this.http.post<string>(this.apiUrl+'/api/currentpayments/send-email/'+id, payment)
    }

    
}