import { Component, OnInit } from '@angular/core';
import { CurrentPaymentsService } from '../shared/services/current-payments.service';
import { Observable } from 'rxjs';
import { Payment } from '../shared/interfaces';

@Component({
  selector: 'app-current-payments-page',
  templateUrl: './current-payments-page.component.html',
  styleUrls: ['./current-payments-page.component.css']
})
export class CurrentPaymentsPageComponent implements OnInit{
  current_payments$:Observable<Payment[]>

  constructor(private currentPaymentService:CurrentPaymentsService){
    
  }

  ngOnInit(): void {
    this.current_payments$ = this.currentPaymentService.fetch()
      
      
   
  }

}
