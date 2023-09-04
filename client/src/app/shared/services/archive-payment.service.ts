import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { environment } from "src/environments/environment";
import { Payment } from "../interfaces";
import { Observable } from "rxjs";

@Injectable({
    providedIn:'root'
})
export class ArchivePaymentsService{

    apiUrl = environment.apiServer

    constructor(private http:HttpClient){

    }

    getAllArchivePayments():Observable<Payment[]>{
        return this.http.get<Payment[]>(this.apiUrl+'/api/archive-payments/')
    }

    deletePayment(id:number):Observable<string>{
        return this.http.delete<string>(this.apiUrl+'/api/archive-payments/'+id)
    }

    fetchPdf(id:number, payment:Payment){
        console.log('rewewrw');

        return this.http.post(this.apiUrl+'/api/archive-payments/fetch-pdf/'+id, payment, {observe:'response', responseType: 'blob' });
    }

    backPayment(id:number):Observable<string>{
        return this.http.post<string>(this.apiUrl+'/api/archive-payments/back-to-current-payments/'+id, {})
    }

}