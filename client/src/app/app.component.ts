import { Component, OnInit } from '@angular/core';
import { AuthService } from './shared/services/auth.services';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  constructor(private auth:AuthService){

  }

  ngOnInit(): void {
    console.log(11111);
    
    const actualToken = localStorage.getItem('auth-token')
    console.log(actualToken, 'actualToken');
    
    if(actualToken !== null){
      console.log(33333);
      
      this.auth.setPlainToken(actualToken)
    }
  }
}
