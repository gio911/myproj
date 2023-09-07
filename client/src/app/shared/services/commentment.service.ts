import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { environment } from "src/environments/environment";
import { Commentment, Payment } from "../interfaces";
import { Observable } from "rxjs";

@Injectable({
    providedIn:'root'
})
export class ComentmentService{

    constructor(private http:HttpClient){

    }

    apiUrl = environment.apiServer


    getAllCommentments(id:number):Observable<Commentment[]>{
        return this.http.get<Commentment[]>(this.apiUrl+'/api/comments/'+id)
    }

    addCommentment(commentment:Commentment):Observable<Commentment>{
        return this.http.post<Commentment>(this.apiUrl+'/api/comments/',commentment)
    }

    deleteCommentment(id:number):Observable<string>{
        return this.http.delete<string>(this.apiUrl+'/api/comments/'+id)
    }

    editCommentment(commentment:Commentment):Observable<Commentment>{
        return this.http.post<Commentment>(this.apiUrl+'/api/comments/', commentment)
    }

}