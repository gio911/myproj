
import { Injectable } from '@angular/core'
import { IAppConfig } from './app-config.model'
import { environment } from './environments/environment'

@Injectable()
export default class AppConfig {
  static settings: IAppConfig

  load = async (): Promise<void> => {
    AppConfig.settings = environment
    console.log(AppConfig.settings);
    
  }
}
