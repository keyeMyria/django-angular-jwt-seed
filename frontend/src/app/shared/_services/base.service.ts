import {Injectable} from '@angular/core';

@Injectable()
export class BaseService {
  base_url = 'http://192.168.0.104:8000/';

  constructor() {
  }

  public getBaseUrl() {
    return this.base_url;
  }
}

