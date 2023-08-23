import { Component, OnDestroy, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { AuthService } from '../shared/services/auth.services';
import { Router } from '@angular/router';
import { Subscription } from 'rxjs';
import { MaterialService } from '../shared/classes/material.service';
import {ToastrService} from 'ngx-toastr'

@Component({
  selector: 'app-register-page',
  templateUrl: './register-page.component.html',
  styleUrls: ['./register-page.component.css']
})
export class RegisterPageComponent implements OnInit, OnDestroy {

  form!:FormGroup
  aSub!:Subscription

  constructor(private auth:AuthService, private router:Router, private toaster:ToastrService){}

ngOnInit(){

  this.form = new FormGroup({
    username: new FormControl(null, [Validators.required, ]),
    email: new FormControl(null, [Validators.required, Validators.email]),
    password: new FormControl(null, [Validators.required, Validators.minLength(6)])
    
    }
  )
}

ngOnDestroy(): void {
  if(this.aSub){
    this.aSub.unsubscribe()
  }
}

onSubmit(){
  this.form.disable()
  this.aSub = this.auth.register(this.form.value).subscribe({
    next:()=>{
    this.toaster.success('Вы успешно зарегистрировались')
    this.router.navigate(['/login'], {
      queryParams:{
        registered:true
      }
    })
    
  },
  
  error:error=>{
    this.toaster.warning(error.error.detail)
    // MaterialService.toast(error.error.detail)
    this.form.enable()
  }
})
  
}

}
